import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from pair_e_data import APPS, APP1_TOTAL, APP2_TOTAL, CHARACTERISTICS, RADAR_OUTPUT, WEIGHTS


def weighted_score(ratings):
    return round(sum(r * w for r, w in zip(ratings, WEIGHTS)), 2)


def polygon_points(center, radius, ratings):
    points = []
    angle_step = (2 * math.pi) / len(ratings)
    start = -math.pi / 2
    for index, rating in enumerate(ratings):
        angle = start + index * angle_step
        scaled = radius * (rating / 5.0)
        x = center[0] + math.cos(angle) * scaled
        y = center[1] + math.sin(angle) * scaled
        points.append((x, y))
    return points


def axis_point(center, radius, index, total):
    angle = -math.pi / 2 + index * ((2 * math.pi) / total)
    x = center[0] + math.cos(angle) * radius
    y = center[1] + math.sin(angle) * radius
    return x, y


def get_font(size, bold=False):
    candidates = [
        "arialbd.ttf" if bold else "arial.ttf",
        "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_text(draw, position, text, font, fill):
    draw.text(position, text, font=font, fill=fill)


def build_radar_chart(output_path=RADAR_OUTPUT):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    width, height = 1600, 1200
    image = Image.new("RGBA", (width, height), (248, 249, 245, 255))
    draw = ImageDraw.Draw(image, "RGBA")

    title_font = get_font(42, bold=True)
    label_font = get_font(24, bold=True)
    body_font = get_font(22)

    center = (520, 620)
    radius = 340
    levels = 5

    bg_color = (223, 231, 224, 255)
    grid_color = (180, 193, 184, 255)
    spotify_line = (28, 185, 84, 255)
    spotify_fill = (28, 185, 84, 90)
    ytm_line = (255, 0, 0, 255)
    ytm_fill = (255, 0, 0, 70)
    axis_color = (90, 100, 95, 255)
    text_color = (34, 39, 36, 255)

    draw.rounded_rectangle((50, 45, width - 50, height - 45), radius=28, fill=bg_color, outline=(205, 214, 207, 255), width=3)
    draw_text(draw, (90, 80), "ISO 25010 Radar Chart: Spotify vs YouTube Music", title_font, text_color)
    draw_text(draw, (90, 135), "Pair E comparison generated from the current workbook draft", body_font, (70, 78, 72, 255))

    total_axes = len(CHARACTERISTICS)
    for level in range(1, levels + 1):
        points = [axis_point(center, radius * (level / levels), idx, total_axes) for idx in range(total_axes)]
        draw.polygon(points, outline=grid_color)

    for idx, characteristic in enumerate(CHARACTERISTICS):
        x, y = axis_point(center, radius, idx, total_axes)
        draw.line((center[0], center[1], x, y), fill=grid_color, width=2)
        lx, ly = axis_point(center, radius + 55, idx, total_axes)
        label = characteristic.replace(" ", "\n")
        bbox = draw.multiline_textbbox((0, 0), label, font=body_font, spacing=4, align="center")
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        draw.multiline_text((lx - text_w / 2, ly - text_h / 2), label, font=body_font, fill=text_color, spacing=4, align="center")

    for level in range(1, levels + 1):
        y = center[1] - (radius * (level / levels))
        draw_text(draw, (center[0] + 8, y - 10), str(level), body_font, axis_color)

    spotify_points = polygon_points(center, radius, APPS["app1"]["ratings"])
    ytm_points = polygon_points(center, radius, APPS["app2"]["ratings"])
    draw.polygon(ytm_points, fill=ytm_fill, outline=ytm_line, width=5)
    draw.polygon(spotify_points, fill=spotify_fill, outline=spotify_line, width=5)

    for point in spotify_points:
        draw.ellipse((point[0] - 6, point[1] - 6, point[0] + 6, point[1] + 6), fill=spotify_line)
    for point in ytm_points:
        draw.ellipse((point[0] - 6, point[1] - 6, point[0] + 6, point[1] + 6), fill=ytm_line)

    legend_x = 980
    legend_y = 180
    draw.rounded_rectangle((legend_x - 30, legend_y - 30, 1490, 1030), radius=22, fill=(255, 255, 255, 190), outline=(210, 216, 212, 255), width=2)
    draw_text(draw, (legend_x, legend_y), "Weighted score summary", label_font, text_color)

    draw.rectangle((legend_x, legend_y + 60, legend_x + 30, legend_y + 90), fill=spotify_fill, outline=spotify_line, width=3)
    draw_text(draw, (legend_x + 45, legend_y + 55), f"Spotify: {APP1_TOTAL:.2f}/5.00", label_font, text_color)
    draw_text(draw, (legend_x + 45, legend_y + 92), "Best for device coverage, usability, and session control", body_font, axis_color)

    draw.rectangle((legend_x, legend_y + 155, legend_x + 30, legend_y + 185), fill=ytm_fill, outline=ytm_line, width=3)
    draw_text(draw, (legend_x + 45, legend_y + 150), f"YouTube Music: {APP2_TOTAL:.2f}/5.00", label_font, text_color)
    draw_text(draw, (legend_x + 45, legend_y + 187), "Best for music-video integration and long-tail content", body_font, axis_color)

    draw_text(draw, (legend_x, legend_y + 260), "Ratings used", label_font, text_color)
    start_y = legend_y + 315
    for idx, characteristic in enumerate(CHARACTERISTICS):
        spotify_rating = APPS["app1"]["ratings"][idx]
        ytm_rating = APPS["app2"]["ratings"][idx]
        line = f"{idx + 1}. {characteristic}: Spotify {spotify_rating} | YouTube Music {ytm_rating}"
        draw_text(draw, (legend_x, start_y + idx * 45), line, body_font, axis_color)

    draw_text(draw, (90, 1085), "Generated by week2/quality_analysis.py", body_font, axis_color)
    image.save(output_path)
    return output_path


def main():
    output = build_radar_chart()
    print(f"APP1_RATINGS = {APPS['app1']['ratings']}")
    print(f"APP2_RATINGS = {APPS['app2']['ratings']}")
    print(f"Spotify weighted total: {weighted_score(APPS['app1']['ratings']):.2f}/5.00")
    print(f"YouTube Music weighted total: {weighted_score(APPS['app2']['ratings']):.2f}/5.00")
    print(f"Radar chart saved to: {output}")


if __name__ == "__main__":
    main()
